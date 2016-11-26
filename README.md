# Pick by Light

## Getting Started

Install and set up mongodb and at least a single member

- Edit `/etc/mongodb.conf` to include 
    ```yaml
    replication:
      replSetName: rs0
    ```
- Edit `/etc/hosts` such that you replace all instances of `127.0.1.1` to `127.0.0.1`
- Restart mongodb with `sudo service mongodb stop` and `sudo service mongodb start`
- Enter the mongo shell `mongo`
    ```bash
    rs.initiate()
    ```
- At this point, you should be seeing `rs0.PRIMARY>` at your prompt, if not, panic

Install Meteor if you have not done yet

```bash
$ curl https://install.meteor.com | sh
```

Install dependencies if you have not done yet

```bash
$ meteor npm install
```

Start the development server

```bash
$ meteor npm start
```

## Building for Production

Create the production build

```bash
$ meteor build ../pbl-meteor-build
```

At this point you will have a compressed file created at `../pbl-meteor-build` which, when uncompressed, will extract
into a directory called `bundle` in which you will find a concise `README.md` file.

Make sure you read the deployment sections from:

- [Meteor documentation](http://docs.meteor.com)
- [Meteor guide](http://guide.meteor.com)

*RTFM!*

