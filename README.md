# matrix-action
A Github Action for sending messages to a Matrix Room.

## Screenshot:
...

## Example Usage:
```yaml
# .github/workflows/matrix-action.yml
on:
  push:
    branches:
      - master

jobs:
  matrix_action_job:
    runs-on: ubuntu-latest
    name: Send Message to Matrix Room
    steps:

    - name: matrix-action
      uses: krazykirby99999/matrix-action@v1

      with:
        homeserver: ${{ secrets.BOT_HOMESERVER }}
        username: ${{ secrets.BOT_USERNAME }}
        access_token: ${{ secrets.BOT_ACCESS_TOKEN }}

        room_id: ${{ secrets.ROOM_ID }}
        message: "#### New Commit:"

```
