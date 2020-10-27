fetch(
    "http://localhost:8000/api-token-auth/",
     {
          mode:'no-cors',
          method: 'POST',
          headers: {
              "Content-type": "multipart/form-data",
            },
          body:JSON.stringify(
              {
                  'username':'serviceaccount','password':'toor'
                }
                )
            }
            )