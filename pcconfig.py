import pynecone as pc

config = pc.Config(
    app_name="Samantha",
    api_url="0.0.0.0:9000",
    # bun_path="/app/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    # env=pc.Env.DEV,
)
