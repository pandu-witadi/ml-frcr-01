module.exports = {
    apps: [

        {
            name: "ml-frcr-fastapi-server",
            cwd: ".",
            script: "env3.8.10/bin/python3",
            args: " -m uvicorn main:app --host 0.0.0.0  --port 5156",
            interpreter: "",
            max_memory_restart: "1G"
        },
        {
            name: "ml-frcr-celery-worker",
            cwd: ".",
            script: "env3.8.10/bin/python3",
            args: " -m celery -A job.task worker -l INFO --concurrency=3",
            interpreter: "",
            max_memory_restart: "1G"
        }
    ]
}
