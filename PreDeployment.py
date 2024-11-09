import os
from dotenv import load_dotenv
load_dotenv()
def CreateAppYamlFile():
    try:
        fileContents = f"""runtime: python312
entrypoint: gunicorn JessePiccione.wsgi:application --bind 0.0.0.0:8080
env_variables:
  DATABASE_ENGINE: '{os.getenv('DATABASE_ENGINE')}'
  DATABASE_NAME: '{os.getenv('DATABASE_NAME')}'
  DATABASE_HOST: '{os.getenv('DATABASE_HOST')}'
  DATABASE_PORT: '{os.getenv('DATABASE_PORT')}'
  DATABASE_USERNAME: '{os.getenv('DATABASE_USERNAME')}'
  DATABASE_PASSWORD: '{os.getenv('DATABASE_PASSWORD')}'
  SECRET_KEY_VAR: '{os.getenv('SECRET_KEY_VAR')}'
  OPENAI_API_KEY: '{os.getenv('OPENAI_API_KEY')}'
automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 10
  min_pending_latency: 30ms
  max_pending_latency: automatic
  max_concurrent_requests: 10
handlers:
- url: /.*
  secure: always
  redirect_http_response_code: 301
  script: auto
        """
        with open('app.yaml', 'w') as f:
            f.write(fileContents.strip())
            f.close()
        print('app.yaml file created or truncated with the following data.', fileContents)
    except:
        print('There was an error generating the App Yaml File check for conflicts and appropriate privileges')
CreateAppYamlFile()