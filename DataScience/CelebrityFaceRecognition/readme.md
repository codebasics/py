![](ui_snapshot.jpg)

In this data science and machine learning project, we classify sports personalities. We restrict classification to only 5 people,
1) Maria Sharapova
2) Serena Williams
3) Virat Kohli
4) Roger Federer
5) Lionel Messi

Here is the folder structure,
* UI : This contains ui website code 
* server: Python flask server
* model: Contains python notebook for model building
* google_image_scrapping: code to scrape Google for images
* images_dataset: Dataset used for our model training

Technologies used in this project,
1. Python
2. Numpy and OpenCV for data cleaning
3. Matplotlib & Seaborn for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI


Here is the video playlist for entire project: https://www.youtube.com/playlist?list=PLeo1K3hjS3uvaRHZLl-jLovIjBP14QTXc


## Running the image scraper

The scraper requires Python, Selenium, Chrome, and a compatible ChromeDriver.
Install the project dependencies first, then run the script from the
`google_image_scrapping` directory.

```bash
pip install -r ../model/requirements.txt
python image_download.py
```

The scraper validates downloaded files before saving them and uses deterministic
filenames to avoid duplicate downloads. Use automated downloading only when it
is permitted by the source website and applicable terms.

## Contributing

Contributions that improve reproducibility, documentation, model evaluation,
accessibility, or code quality are welcome. Keep pull requests focused and
include a short explanation of what changed and how it was tested.
