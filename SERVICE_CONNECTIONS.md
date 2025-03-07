# Setup service connections

## Reporting code coverage via CodeCov (codecov.io)

1. Sign-Up at https://app.codecov.io/
2. Configure via https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen
3. Select (o) Repository token. Copy value of `CODECOV_TOKEN` into your clipboard
4. Goto https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/settings/secrets/actions/new and create a new repository secret called `CODECOV_TOKEN`, pasting the token from your clipboard as value
5. Re-run the `CI / test` GitHub job in case you tried before and it failed as Codecov was not yet wired up

## Analyzing code quality and security analysis via SonarQube cloud (sonarcloud.io)

1. Sign-Up at https://sonarcloud.io
2. Grant access to your new repo via https://github.com/settings/installations -> Configure
3. Goto https://sonarcloud.io/projects/create and select the repo
4. Select Previous Code when prompted
5. Configure by going to https://sonarcloud.io/project/configuration?id=helmut-hoffer-von-ankershoffen_brave-search-python-client and clicking on "With GitHub Actions". Copy the value of `SONAR_TOKEN` into your clipboard.
6. Goto https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/settings/secrets/actions/new and create a new repository secret called `SONAR_TOKEN`, pasting the token from your clipboard as the value
7. Goto https://sonarcloud.io/project/settings?id=helmut-hoffer-von-ankershoffen_brave-search-python-client and select "Quality Gate" in the left menu. Select "Sonar way" as default quality gate.
8. Re-run the `CI / test` GitHub job in case you tried before and it failed as SonarQube was not yet wired up

## Generating and publishing documentation via ReadTheDocs (readthedocs.org)

1. Sign-Up at https://readthedocs.org/
2. Goto https://app.readthedocs.org/dashboard/import/ and search for your repo by enterin brave-search-python-client in the search bar
3. Select the repo and click Continue, then Next.
4. On https://app.readthedocs.org/projects/brave-search-python-client/ wait for the build of the documentation to finish
5. Goto https://brave-search-python-client.readthedocs.io/en/latest/

## Publishing package to Python Package Index (pypi.org)

1. Execute `uv run build`. This will generate the build files (wheel and tar.gz) in the `dist` folder
2. Sign-Up at https://pypi.org/
3. Goto https://pypi.org/manage/account/ and create an API token of scope "Entire account", calling it brave-search-python-client. Copy the value of the token into your clipboard.
4. Execute `uv run publish`, entering __token__ as username and paste the token from your clipboard as password. This will register your package on PyPI and upload the build files
5. Goto https://pypi.org/manage/account/ again and delete the previously created token brave-search-python-client of scope "Entire account".
6. Now create an new API token, again called brave-search-python-client, but this time of scope "Project: brave-search-python-client". Copy the token into your clipboard.
7. Goto https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/settings/secrets/actions/new and delete the previously created token.
8. Then create a new repository secret called `UV_PUBLISH_TOKEN`, pasting the token from your clipboard as value
9. In case your `CI / test` job passed, and you are ready to release and publish, bump the version of your project by executing `bump`. In case you tried before completing this setup script, you can as well go to https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/package-build-publish-release.yml, click on the failed job, and re-run.

## Publishing Docker images to Docker Hub (docker.io)

1. Sign-Up at https://hub.docker.com/
2. Click on your avatar or profile pic and copy the username below that into your clipboard.
3. Goto https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/settings/secrets/actions/new and create a new repository secret called `DOCKER_USERNAME`, setting your username at Docker Hub as the value
4. Goto https://app.docker.com/settings/personal-access-tokens/create and create a new access token setting the description to brave-search-python-client, permissions Read & Write & Delete. Copy the value of the token into your clipboard.
5. Goto https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/settings/secrets/actions/new and create a new repository secret called `DOCKER_PASSWORD`, pasting the token from your clipboard as the value
6. In case your `CI / test` job passed, and you are ready to release and publish, bump the version of your project by executing `bump`. In case you tried before completing this setup script, you can as well go to https://github.com/helmut-hoffer-von-ankershoffen/brave-search-python-client/actions/workflows/package-build-publish-release.yml, click on the failed job, and re-run.

## Publishing Docker images to GitHub Container Registry (ghcr.io)

1. This just works, no further setup required.
2. Just `bump` to release and publish.

## Streamlit app (streamlit.io)

1. Sign-up at https://streamlit.io
2. In settings connect your GitHub account
3. Goto https://share.streamlit.io/new and click "Deploy a public app from GitHub"
4. Select the brave-search-python-client repo, for "Main file path" select `examples/streamlit.py`, for App URL enter `brave-search-python-client`.streamlit.app. Click "Deploy"
5. Goto https://brave-search-python-client.streamlit.app
