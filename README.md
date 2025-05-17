<!-- start header -->
# ThePizzaConundrumProblem
<!-- end header -->





## Description
<!-- start description -->
How definitie analysis of which pizza is the best in south africa
<!-- end description -->

## Getting the Project/CodeBase Setup
### Install VsCode 
I use VsCode to edit my code. This repo contains helpful configuration settings and recommended extensions in the `.vscode` folder so i'd recommend using VsCode as well if you want the most semaless experience. I don't test anything with other IDE's but it might work on others, however don't quote me on that.
you can find the download for VsCode here 
[https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
Once VsCode is installed you should be able to clone the repository from github


### Install uv
We'll use uv for package managemnt and dependency resolution. 
so first we need to install it. 
to do this we can use the command line script below
[Script_WingetInstallUv.bat](Script_WingetInstallUv.bat)

### Install all packages
Next we need to install all the packages/dependecies we use (e.g. pandas, plotly, etc).
Its best practise to do this in a virtual environment. Luckily `uv` does a lot of this for us using its uv sync command. 
To do this we can run the command line script below
[Script_UvSync.bat](Script_UvSync.bat)



