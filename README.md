# ukr_eng_patterns
This project can help to teach or to learn English, Ukrainian or any other language.
Tutorial for Goolge's API https://www.youtube.com/watch?v=ddf5Z0aQPzY

1. First part of code set everything up for instance of Google sheets client.
![Screen Shot 2023-03-11 at 12 19 00](https://user-images.githubusercontent.com/106767931/224468633-c02bc50a-dc8d-4f97-bb75-02a4b650a8c0.png)


2. Second part is represent input data for geteration sentences and its positions in spreadsheet.
![Screen Shot 2023-03-11 at 11 59 05](https://user-images.githubusercontent.com/106767931/224468536-1147a242-e4be-431d-9dab-2e65e12871f9.png)


3. Third part of code is contained two for loops. 
- First for loop using update_cell method to send generating data to google sheet. It looks as one column. Each cell filled with one sentence.
- Second for loop using update_cell method to send formula GOOGLETRANSLATE to column of google sheet on the left of column filled with previous for loop.
![Screen Shot 2023-03-11 at 12 23 39](https://user-images.githubusercontent.com/106767931/224469102-c7160cdc-5ed9-46cf-8724-306368ca4485.png)

result:

![gif_result](https://user-images.githubusercontent.com/106767931/224469795-a35f7280-5eaa-49ea-8fe5-a93d9aa240a5.gif)
