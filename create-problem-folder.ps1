param(
    [int]$number,
    [string]$path = "./leetcode"
)

# Construct the folder name and path
$folderName = "$number"
$folderPath = Join-Path -Path $path -ChildPath $folderName

# Create the folder
if (-Not (Test-Path -Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath
}

# Create the files
New-Item -ItemType File -Path (Join-Path -Path $folderPath -ChildPath "solution.py") | Out-Null
New-Item -ItemType File -Path (Join-Path -Path $folderPath -ChildPath "problem.md") | Out-Null
New-Item -ItemType File -Path (Join-Path -Path $folderPath -ChildPath "solution.md") | Out-Null

Write-Output "Folder and files created at $folderPath"

git add $folderPath