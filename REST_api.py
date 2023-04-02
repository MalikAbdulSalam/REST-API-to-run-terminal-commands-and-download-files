# using flask_restful
from flask import Flask, jsonify, request,send_from_directory,send_file
from flask_restful import Resource, Api
import os
import zipfile


# creating the flask app
app = Flask(__name__)

DOWNLOAD_DIRECTORY = "./json"
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):

		return jsonify({'message': 'bismillah'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class detection_geojson(Resource):

	def get(self):
		# Zip file Initialization
		zipfolder = zipfile.ZipFile('Downloadfiles.zip', 'w', compression=zipfile.ZIP_STORED)  # Compression type

		# zip all the files which are inside in the folder
		for root, dirs, files in os.walk('./json/'):
			for file in files:
				zipfolder.write('./json/' + file)
		zipfolder.close()

		return send_file('./Downloadfiles.zip',
						 mimetype='zip',
						 as_attachment=True)

		# Delete the zip file if not needed
		#os.remove("Audiofiles.zip")


# adding the defined resources along with their corresponding urls

class com_txt(Resource):

	def get(self, name):

		f = open("./api_commands.sh", "w")
		f.write(name)
		f.close()

		os.popen('sh ./api_commands.sh')
		return jsonify({'your command text is ': name})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(detection_geojson, '/geojson')
api.add_resource(com_txt, '/comand_text/<string:name>')



# driver function
if __name__ == '__main__':

	app.run(debug = True)
 