# UnityCloud Collaboration CLI

Collabi provides command line (console) access to the
[UnityCloud Collaboration Service](https://unity3d.com/services/collaborate). Collaborate is a
simple way for small teams to save, share, and sync their Unity project. It’s cloud hosted and easy
to use so the entire team can contribute to the project, regardless of location or role.

### Why Collabi?

The Unity Editor has built-in support for working with the Collaboration Service, but there are some
edge cases and workflows that more advanced users require. Collabi can help with the following
scenarios (each case assumes collabi is executed from the root of an existing project).

[ ***NOTE:*** Collabi should not be run while the Unity Editor is working with the same project on the same machine. ]

* Cherry pick one or more files to publish or update.
  * `collabi project . upload Assets/Scenes/MyScene* 'fix just my scene'`

* Revert all or part of a project to a known working version.
  * `collabi project . --revision 12345678 download_sync Assets`
  * `collabi project . upload_sync Assets 'revert all assets back to version 12345678'`

* Save work outside of the `Assets` or `ProjectSettings` folders.
  * `collabi project . upload_sync MyRawArt 'work in progress'`

* Get the latest revision info in an easy-to-parse form for scripts.
  * `collabi --format simple project . info`

* Get version history information for one or all files.
  * `collabi project . history`

* Get a listing of all or some of the files saved in the cloud.
  * `collabi project . list --recursive --human --summarize`

* Get a listing of user, org, and project info.
  * `collabi user me`, `collabi user orgs`, `collabi user projects`

* Runs anywhere Python can (e.g. Mac OS X, Windows, and Linux).
  * Collabi could be used to assist in automated build systems for project retrieval.

And much, much more. Check out [`collabi --all-help`](./all_help.md) for a full list of actions
available.

### What does Collabi do differently?

As an advanced tool, Collabi assumes the user understands the implications of invoking the actions
available. **_Collabi will not report any conflicts._** Instead, it expects to help a user with the
following:

> I want to synchronize what is in this directory to the cloud. I want the cloud to look exactly
> like this directory.

* In other words, upload all files found in a directory on the local system to the cloud. Files
  already in the cloud will be replaced. Files in the cloud but not on the local system are deleted
  (but preserved in history, so it's possible to revert to earlier versions).

> I want to synchronize what is in the cloud to this directory. I want this directory to look
> exactly like the cloud.

* In other words, download all files found in a cloud directory to the local system. Files already
  in the local system will be sent to the system trash and replaced with the cloud versions. Files
  on the local system but not in the cloud are sent to the system trash (so it's possible to revert
  to an earlier version).

### How to install?

Choose one of the following methods:

* Trust in [PyPI](https://pypi.python.org/pypi/collabi).
  * OS X or Linux: `pip install collabi`
  * Windows (if using Python 2.7.9 or later): `python -mpip install collabi`
    * Note: To access pip-installed "binaries" the `Scripts` directory needs to be in the `PATH`
      environment variable, something like the following...
      * `set PATH=%PATH%;C:\Python27;C:\Python27\Scripts`

* Source is King! Download (or clone)
  [this repository](https://github.com/UnityTech/unitycloud-collab-cli) and run `python -mcollabi
  ...` or `make install` (requires pip).

* Binaries are where it's at! ***Python is not required when using these.*** Each build is native to
  the platform and has minimal dependencies; everything is self-contained. Grab one from the
  [latest releases](https://github.com/UnityTech/unitycloud-collab-cli/releases) for:
  * Mac OS X
  * Windows
  * Linux

### Where is more help?

* Breeze through all the usage to see if what you're after is already available:
  [`collabi --all-help`](./all_help.md)
* Check out the source, wiki, and issues:
  [https://github.com/UnityTech/unitycloud-collab-cli](https://github.com/UnityTech/unitycloud-collab-cli)
  * We also gladly accept pull requests!
* Forums are a great resource to see if others have already asked the same question:
  [http://forum.unity3d.com/forums/collaborate.98/](http://forum.unity3d.com/forums/collaborate.98/)
* Finally, send an email to collabsupport@unity3d.com and let us know what you need!
