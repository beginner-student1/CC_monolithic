# from locust import task, run_single_user
# from locust import FastHttpUser


# class browse(FastHttpUser):
#     host = "http://localhost:5000"
#     default_headers = {
#         "Accept-Encoding": "gzip, deflate, br, zstd",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Connection": "keep-alive",
#         "DNT": "1",
#         "Sec-GPC": "1",
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
#     }

#     @task
#     def t(self):
#         with self.client.request(
#             "GET",
#             "/browse",
#             headers={
#                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
#                 "Host": "localhost:5000",
#                 "Priority": "u=0, i",
#                 "Sec-Fetch-Dest": "document",
#                 "Sec-Fetch-Mode": "navigate",
#                 "Sec-Fetch-Site": "cross-site",
#                 "Upgrade-Insecure-Requests": "1",
#             },
#             catch_response=True,
#         ) as resp:
#             pass
       

# if __name__ == "__main__":
#     run_single_user(browse)

from locust import task, run_single_user
from locust import FastHttpUser


class Browse(FastHttpUser):
    # Set the base host for requests
    host = "http://localhost:5000"
    
    # Default headers for requests
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def browse_products(self):
        """
        Simulates a user browsing products.
        Checks if the response is successful (200 OK) and logs failures otherwise.
        """
        # Perform a GET request to the browse endpoint
        with self.client.get(
            "/browse",
            headers=self.default_headers,
            catch_response=True,
        ) as response:
            # Validate response
            if response.status_code == 200:
                # Mark as success
                response.success()
            else:
                # Log the failure with status code
                response.failure(f"Failed with status code {response.status_code}")

if __name__ == "__main__":
    # Ensure the correct class name is passed to run_single_user
    run_single_user(Browse)