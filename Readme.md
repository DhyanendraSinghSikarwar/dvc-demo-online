## Adding the remote dir (local folder) in DVC like git
dvc remote add -d myremote /home
/dev37/Documents/campusx/storage-for-dvc-demo/campusx
## Switch between experiments
in git using sha id: git log --> git checkout sha_id
in dvc, to get respective data : dvc checkout

## for other developer
 if other developer want to work on this project, first he/she will clone repo, then all the code will be cloned
 for fetching data, 
 first run:  dvc fetch   --> this will fetch data to cache/staging
 then run: dvc checkout
 or, run single command: dvc pull  --> to fetch and checkout together