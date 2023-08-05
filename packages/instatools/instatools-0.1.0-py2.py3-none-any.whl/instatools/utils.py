from io import BytesIO
import PIL.Image


def get_image_size():
    """Get the size (width, height) of an image"""
    pass


def image_from_data(data):
    """Create PIL.Image object from raw response data"""
    return PIL.Image.open(BytesIO(data))


def image_from_path(path):
    """Create PIL.image object from path"""
    return PIL.Image.open(path)

# from concurrent.futures import ThreadPoolExecutor, as_completed
# from io import BytesIO
# from ratelimiter import RateLimiter
#
# import PIL.Image
# import json
# import requests
# import time
#
#
# def _set_image_data(post, data):
#     post.image = data
#
#
# class Post:
#     def __init__(self, **params):
#
#         self._image = None
#
#     @property
#     def image(self):
#         while self._image is None:
#             time.sleep(1e-3)
#         return self._image
#
#     @image.setter
#     def image(self, data):
#         self._image = PIL.Image.open(BytesIO(data))
#
#
# class PostDownloader:
#     def __init__(self, n_threads=40):
#         self.pool = ThreadPoolExecutor(n_threads)
#         self.limiter = RateLimiter(5000, 3600)
#         self.futures = set()
#
#     def get_image(self, post):
#         f = self.pool.submit(self.download_image_data, post.url)
#         f.add_done_callback(lambda fut: _set_image_data(post, fut.result()))
#         self.futures.add(f)
#
#     def close(self):
#         for f in self.futures:
#             if not f.done():
#                 f.cancel()
#             self.futures.remove(f)
#
#         self.pool.shutdown()
#
#     def download_image_data(self, url):
#         with self.limiter:
#             resp = requests.get(url)
#             data = resp.content
#         return data
