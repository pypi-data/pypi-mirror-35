# Orgreviewer

Orgreviewer is tool for managing [itsyou.online](https://itsyou.online) members. The primary goal of the tool is to list, remove and replace users in organizations.

## Installation

* Git: install by cloning this repo, `cd` to the repo's root and execute `pip3 install .`

* pip install

## Commands

### list_all_members

`list_all_members` lists all members in the tree of the organization supplied in the config file

#### Config file:
The yaml config file for this command should look something like this

```yaml
client_id: <itsyou.online application ID>
client_secret: <itsyou.online application secret>
organization: test_organization
```
#### Flags

* `-c, --config-file`: config file location (if not provided, it wil use `./config.yaml`)
* `-s, --summary`: print summary of found users


#### Usage

```sh
orgreviewer list_all_members -c config.yaml -s
```

Output:
```sh
test_organization:
        my_account@gig.tech (owner)
test_organization.sub1:
        my_account@gig.tech (owner)
        user1@gig.tech (member)
test_organization.sub2:
        user2@gig.tech(owner)
test_organization.sub3:
        my_account@gig.tech (owner)
        user1@gig.tech (member)
        user2@gig.tech(owner)
test_organization.sub3.test1:
        my_account@gig.tech (owner)
        user1@gig.tech (member)

--Summary-- # only outputted with the -s flag
- Users:
my_account@gig.tech

- Organizations:
```

### remove_members_blacklist

`remove_members_blacklist` removes members in the organisation tree that are listed in the blacklist file supplied in the config file

#### Config file:

```yaml
client_id: <itsyou.online application ID>
client_secret: <itsyou.online application secret>
organization: test_organization
black_list_file: blacklist.txt
replace_member:  my_account@gig.tech #this user is used to replace a member which is the only owner that's being removed from an organization
```

The blacklist file is a simple text file that contains a line seperated list of users that need to be removed from the organization's tree

```txt
user1@gig.tech
user2@gig.tech
```

#### Flags

* `-c, --config-file`: config file location (if not provided, it wil use `./config.yaml`)

#### Usage

```sh
orgreviewer remove_members_blacklist -c config.yaml
```

Before a user is removed, the script will prompt to confirm to remove the member.

When the user is the last owner of an organization, the script will additionally prompt if the user should be replaced. If declined, the user will not be removed.
