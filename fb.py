# To use the Facebook Ad Library API to get a list of current running image ads and store the images in Python, we will first need to obtain an access token with the necessary permissions to access the Ad Library. We can then use the access token to make a request to the Ad Library API endpoint to retrieve the list of ads.

# Once we have the list of ads, we can loop through each ad and check if it is an image ad. If it is an image ad, we can download the image and store it locally on our system.



import requests

# Set access token with permission to access Ad Library
access_token = 'YOUR_ACCESS_TOKEN'

# Set Ad Library API endpoint URL
ad_library_url = 'https://graph.facebook.com/v8.0/ads_archive'

# Set parameters for API request, including access token and ad status (running)
params = {
    'access_token': access_token,
    'ad_status': 'RUNNING',
    'search_terms':'electronics',
    'ad_reached_countries':['US']
}

# Make API request to get list of current running ads
response = requests.get(ad_library_url, params=params)
ads = response.json()

print(ads)
# Loop through each ad in the list of ads
for ad in ads:
    # Check if ad is an image ad
    if ad['creative_type'] == 'IMAGE':
        # Download image from ad URL
        image_response = requests.get(ad['creative_url'])
        
        # Save image to local directory
        with open('ad_images/{}.png'.format(ad['id']), 'wb') as f:
            f.write(image_response.content)
