# matrix-action
A Github Action for sending messages to a Matrix Room.

## Screenshot:
...

## Example Usage:
```yaml

- name: matrix-action
  uses: krazykirby99999/matrix-action@v1
  with:
  
    homeserver: "https://matrix.org"
    username: "user"
    access_token: "syt_a3J...Ntg"

    room_id: "!Stk...XbP:matrix.org"
    message: "# Commit Successful!"

```