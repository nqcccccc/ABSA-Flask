
# ABSA-FLASK

ABSA-Flask is a website used to deploy PhoBert to solve the aspect-based sentiment analysis problem for restaurant domain.  
- Technologies:
	- Deep learning: Huggingface, Pandas, Sklearn, Tensorflow.
	- Back-end: using Flask to create API for client request.
	- Front-end: HTML5, SCSS, JS, Bootstrap.
## Steps to execute 
- Create venv 
- Install requirements from `requirements.txt`
- Set up `FLASK_APP` and `FLASK_ENV` (optional but usefule for later dev)
    ```
        set Flask_APP=main.py
        set Flask_ENV=development
    ```
- Make sure you are in the root folder then open Terminal here 
- `flask run`
## Deploy with Docker
```
	docker pull nqcccccc/absa-flask
	docker run -p 5000:5000 nqcccccc/absa-flask
```
## Author
[Cuong Q. Nguyen] & [Nhut M. Nguyen]

[Cuong Q. Nguyen]: https://linkedin/in/nguyenquoccuonggg
[Nhut M. Nguyen]: https://github.com/NhutNguyen236