# matrix-commit
A Github Action for sending messages to a Matrix Room.

## Screenshot:
![Example Image](./example.png)

## Example Usage:
```yaml
# .github/workflows/matrix-commit.yml
on:
  push:
    branches:
      - master

jobs:
  matrix_action_job:
    runs-on: ubuntu-latest
    name: Send Message to Matrix Room
    steps:

    - name: Checkout
      uses: actions/checkout@v2

    - name: matrix-commit
      uses: krazykirby99999/matrix-commit@v1

      with:
        homeserver: ${{ secrets.BOT_HOMESERVER }}
        username: ${{ secrets.BOT_USERNAME }}
        access_token: ${{ secrets.BOT_ACCESS_TOKEN }}

        room_id: ${{ secrets.ROOM_ID }}
        message: "#### New Commit:"

```

## Notes:

### Syntax:
- The homeserver should be in the form of "https://domain.tld"
- The username should be the username, not the user id. ("krazykirby99999", not "@krazykirby99999:matrix.org")
- The room_id should be the internal room id of the room, not the published address. ("!QQpfJfZvqxbCfeDgCj:matrix.org", not "#thisweekinmatrix:matrix.org") This can be found under Room Options > Advanced > Room Information in the Element Client.

### Other
- If the room_id is not specified, the bot will send the message to all joined rooms.
- If the message is not specified, it will default to "Commit:".
- The bot will join all invited rooms upon the start of an action.