## how to begin

- once every dependency get installed do the following
- be in a project folder
- type the following code:

```
prisma init
```

- once every configuration ends then start with following code
  - **do not forget** to configure `.env` file, as of now git is ignored in commit
```
prisma generate
```

```
prisma db push
```

## how to start
run the following code
```
uvicorn main:app --reload
```
