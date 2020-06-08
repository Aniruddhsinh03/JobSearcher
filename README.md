# JobSearcher

This is a Scrapy project to scrape job information from  https://newyork.craigslist.org/d/automotive-services/search/aos.

This project is only meant for educational purposes.

## Element Selection

Job Listing Website


![Image of Website](https://github.com/Aniruddhsinh03/JobSearcher/blob/master/screenshots/job_1.jpg)

Extract Job Urls


![Image of jobUrls](https://github.com/Aniruddhsinh03/JobSearcher/blob/master/screenshots/job_2.jpg)

Extract Date


![Image of Date](https://github.com/Aniruddhsinh03/JobSearcher/blob/master/screenshots/job_3.jpg)

Extract Thumbs


![Image of Thumbs](https://github.com/Aniruddhsinh03/JobSearcher/blob/master/screenshots/job_4.jpg)


Extract Job Posting Body


![Image of JobPostingBody](https://github.com/Aniruddhsinh03/JobSearcher/blob/master/screenshots/job_5.jpg)


## Extracted data

This project extracts quotes, combined with the respective author names and tags.
The extracted data looks like this sample:

           {
             "date": "2020-06-08 02:00",
             "link": "https://newyork.craigslist.org/stn/aos/d/staten-island-mobile-auto-body-repair/7137824388.html",
             "text": "mobile auto body repair 60% off shop price",
             "compensation": null,
             "type": null,
             "images": [
             "https://images.craigslist.org/00W0W_dX9Njz7JLwE_0t20t2_600x450.jpg",
             "https://images.craigslist.org/00p0p_85S5teL5luk_0t20t2_600x450.jpg",
             "https://images.craigslist.org/01010_51Z32ESXNL7_0t20t2_600x450.jpg",
             "https://images.craigslist.org/00b0b_81REHtuVZWo_0t20t2_600x450.jpg"
                       ],
             "address": [
             "\n        ",
            "\nmobile auto body repair we come to you same day service all jobs big or small satisfaction guaranteed 60% shop price      r            ubber & plastic bumper repair all size dents rust holes scuff marks scratches faded paint repair fiber glass repair         headlight restoration color matching & blending part replacement & installation call or text for free estimate 917.454.4453"
                        ]
              }

## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    jonSearcherSpider

Spider extract the data from quotes page and visit author hyperlink and extract auther infomation also.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl jonSearcherSpider

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl jonSearcherSpider -o output.json
