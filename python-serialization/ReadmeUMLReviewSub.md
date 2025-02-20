# Sequence Diagram: review submission
Users can leave reviews for places they have visited, including a rating and a comment.
This sequence diagram illustrates the process to submit a review for a place by the user in the HBnB platform. The diagram shows the complete flow from initial user data submission through validation, including error handling.

Image:
Pour info, la syntaxe pour intégrer une image qui se trouve dans le même dossier que le README.md
![Description de l'image](nom_du_fichier.png)


### Main Success Scenario
1. User sends a POST request to the API to submit a comment.
2. The API checks if the user is authenticated.
3. The API forwards the request to the BusinessLogic for validation and processing of the review.
4. The BusinessLogic validates the content of the review.
5. The BusinessLogic inserts the review into the database.
6. The database returns a success response (with the review ID) to the BusinessLogic.
7. The BusinessLogic forwards the review ID to the API.
8. The API returns a 201 Created response to the user with the review ID.

### Alternative Flow
1. **User not logged in**
   - the API stops the process and returns a 401 Unauthorized response directly to the user.

2. **Review validation fails**
   - The BusinessLogic returns a 400 Bad Request response to the API because the review validation fails.
   - The API returns a 400 Bad Request response to the user.

. **Database insertion fails**
   - API returns a 500 Internal Server Error.
   - Ensures proper error handling for system failures
