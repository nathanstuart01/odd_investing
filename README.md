# odd_investing
Getting Started:
1. Install Docker: `https://docs.docker.com/get-docker/` 
2. Pull a postgres docker image: `docker pull postgres`
3. Run postgres docker container: `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`
4. Create a virtual env: `python3 -m venv name_of_virtual_env`
5. Activate virtual env: `python3 source name_of_virtual_env/bin/activate`
6. Install pipenv: `pip install pipenv`
7. Install pip file packages `pipenv install`
8. Create .env file from .example.env
9. Export .env values `export $(cat .env | xargs)`
10. Run api: `make local`
11. Navigate to your local api swagger docs to interact with api: `http://127.0.0.1:8000`
12. test test git pull
13. test on master 
14. test v2 master
14. test v3 master
# some notes about my feature
15. stuff added
16. one last stuff added
17. added something to test tagging