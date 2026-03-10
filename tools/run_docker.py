from pathlib import Path
try:
    import docker
except ImportError:
    raise ImportError(
        "The 'docker' package is required to run this script. "
        "Please install it using 'pip install docker'."
    )

REPO = Path(__file__).resolve().parent.parent
repo_str = REPO.as_posix()

if __name__ == "__main__":
    client = docker.from_env()
    print("Docker client initialized successfully.")

    print("Building Docker image...")
    client.images.build(path=".", dockerfile="tools/Dockerfile", tag="thomasinovic/datacamp33:v2", nocache=True)
    print("Docker image built successfully with tag 'thomasinovic/datacamp33:v2'.")

    print("Running Docker container...")
    logs = client.containers.run(
        image="thomasinovic/datacamp33:v2",
        command="python3 /app/ingestion_program/ingestion.py",
        remove=True,
        name="ingestion",
        user="root",
        volumes=[
            f"{repo_str}/ingestion_program:/app/ingestion_program",
            f"{repo_str}/dev_phase/input_data:/app/input_data",
            f"{repo_str}/ingestion_res:/app/output",
            f"{repo_str}/solution:/app/ingested_program",
        ]
    )
    print(logs.decode("utf-8"))
    logs = client.containers.run(
        image="thomasinovic/datacamp33:v2",
        command="python3 /app/scoring_program/scoring.py",
        remove=True,
        name="scoring",
        user="root",
        volumes=[
            f"{repo_str}/scoring_program:/app/scoring_program",
            f"{repo_str}/dev_phase/reference_data:/app/input/ref",
            f"{repo_str}/ingestion_res:/app/input/res",
            f"{repo_str}/scoring_res:/app/",
        ]
    )
    print(logs.decode("utf-8"))
    print("Docker container ran successfully.")
