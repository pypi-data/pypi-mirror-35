# scalar

Python Matrix library, built on the [Matrix Client-Server SDK](https://github.com/matrix-org/matrix-python-sdk)

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
    "configurations": {
        "scriptwire": {
            "default"   : True,
            "homeserver": "https://matrix.example.pro:8448",
            "username"  : "scriptwire",
            "passcode"  : "qo3i4tbc35wgtt4gbwikgvtib3ctgt7bgi3rgw",
            "room_alias": "!cgOnMzaBWCLjBnhGiB:matrix.example.org"
        }
    },
    "version_config": "2018-08-23T1930Z"
}
```

There can be multiple configurations, such as for separate accounts. One configuration must be set as the default if a configuration is not specified on setup. A room must be one to which the account has been invited.

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

[megaparsex](https://github.com/wdbm/megaparsex) can be used with scalar to send data via messages, in ways like the following:

```Python
import megaparsex
import scalar
scalar.alert(message=megaparsex.report_IP())
scalar.alert(message=megaparsex.report_system_status())
scalar.alert(message=megaparsex.report_METAR("EGPF"))
```

# upload and send text, files, audio, images and video

```Python
import scalar
scalar.send_text("test")
scalar.send_file("test.csv")
scalar.send_audio("test.ogg")
scalar.send_image("test.gif")
scalar.send_video("test.mp4")
```
