# scalar

Python Matrix library

# setup

```Bash
pip install scalar
```

Create a configuration.

```Bash
mkdir -p ~/.config/scalar
touch ~/.config/scalar/config.yaml
```

The configuration file contents should be like the following:

```YAML
{
    "homeserver": "https://matrix.example.pro:8448",
    "username"  : "scriptwire",
    "passcode"  : "qo3i4tbc35wgtt4gbwikgvtib3ctgt7bgi3rgw",
    "room_alias": "!cgOnMzaBWCLjBnhGiB:matrix.example.org"
}
```

The room must be one to which the account has been invited.

# alert

An alert message can be sent on the terminal, in a way like the following:

```Bash
scalar_alert --message="This is an alert message."
```

An alert message can be send in Python, in a way like the following:

```Python
import scalar
scalar.alert(message="alert")
```
