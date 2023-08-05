from requests_toolbelt import MultipartEncoder
from time import time
from .api import ApiMethod
from ..utils import image_from_path


class Upload:
    def __init__(self, api=None):
        self.api = api

    def album(self):
        pass

    def photo(self, photo, caption=None, upload_id=None):
        img = image_from_path(photo)
        upload_id = upload_id or int(time())
        data = self.api.session.upload_data_photo(upload_id, open(photo, 'rb'))
        m = MultipartEncoder(data, boundary=str(self.api.session._uuid))
        headers = self.api.session.upload_headers(m.content_type)
        resp = self.api.session._session.post(
            self.api.session.url('upload_photo'),
            data=m.to_string(), headers=headers
        )

        if resp.status_code == 200:
            if self.configure_photo(upload_id, caption, img.width, img.height):
                return self.expose()

        return resp

    def video(self, video, thumbnail=None, caption=None):
        data = {}

        return ApiMethod(self.api).action('upload_video', data=data)

    def configure_album(self):
        pass

    def configure_photo(self, upload_id, caption, width, height):
        data = self.api.session.configure_data(
            width, height, upload_id, caption)
        data.update(self.api.session.configure_data_photo(width, height))
        return ApiMethod(self.api).action('configure', data=data)

    def configure_video(self, upload_id, caption,
                        width, height, duration, thumbnail):
        data = {}

        return ApiMethod(self.api).action('configure',
                                          params={'video': '1'}, data=data)

    def expose(self):
        return ApiMethod(self.api).action('expose', data={
            'id': self.api.username_id,
            'experiment': 'ig_android_profile_contextual_feed'
        })


# def uploadPhoto(self, photo, caption=None, upload_id=None, is_sidecar=None):
#     if upload_id is None:
#         upload_id = str(int(time.time() * 1000))
#     data = {'_uuid': self.uuid,
#             '_csrftoken': self.token,
#             'upload_id': upload_id,
#             'image_compression':
# '{"lib_name":"jt","lib_version":"1.3.0","quality":"87"}',
#             'photo': ('pending_media_%s.jpg' % upload_id,
#                       open(photo, 'rb'),
#                       'application/octet-stream',
#                       {'Content-Transfer-Encoding': 'binary'})
#             }
#     if is_sidecar:
#         data['is_sidecar'] = '1'
#     m = MultipartEncoder(data, boundary=self.uuid)
#     self.s.headers.update({'X-IG-Capabilities': '3Q4=',
#                            'X-IG-Connection-Type': 'WIFI',
#                            'Cookie2': '$Version=1',
#                            'Accept-Language': 'en-US',
#                            'Accept-Encoding': 'gzip, deflate',
#                            'Content-type': m.content_type,
#                            'Connection': 'close',
#                            'User-Agent': self.USER_AGENT})
#     response = self.s.post(self.API_URL +
# "upload/photo/", data=m.to_string())
#     if response.status_code == 200:
#         if self.configure(upload_id, photo, caption):
#             self.expose()
#     return False
#
# def uploadVideo(self, video, thumbnail,
# caption=None, upload_id=None, is_sidecar=None):
#     if upload_id is None:
#         upload_id = str(int(time.time() * 1000))
#     data = {'upload_id': upload_id,
#             '_csrftoken': self.token,
#             'media_type': '2',
#             '_uuid': self.uuid}
#     if is_sidecar:
#         data['is_sidecar'] = '1'
#     m = MultipartEncoder(data, boundary=self.uuid)
#     self.s.headers.update({'X-IG-Capabilities': '3Q4=',
#                            'X-IG-Connection-Type': 'WIFI',
#                            'Host': 'i.instagram.com',
#                            'Cookie2': '$Version=1',
#                            'Accept-Language': 'en-US',
#                            'Accept-Encoding': 'gzip, deflate',
#                            'Content-type': m.content_type,
#                            'Connection': 'keep-alive',
#                            'User-Agent': self.USER_AGENT})
#     response = self.s.post(self.API_URL +
# "upload/video/", data=m.to_string())
#     if response.status_code == 200:
#         body = json.loads(response.text)
#         upload_url = body['video_upload_urls'][3]['url']
#         upload_job = body['video_upload_urls'][3]['job']
#
#         videoData = open(video, 'rb').read()
#         # solve issue #85 TypeError: slice i
# ndices must be integers or None or have an __index__ method
#         request_size = int(math.floor(len(videoData) / 4))
#         lastRequestExtra = (len(videoData) - (request_size * 3))
#
#         headers = copy.deepcopy(self.s.headers)
#         self.s.headers.update({'X-IG-Capabilities': '3Q4=',
#                                'X-IG-Connection-Type': 'WIFI',
#                                'Cookie2': '$Version=1',
#                                'Accept-Language': 'en-US',
#                                'Accept-Encoding': 'gzip, deflate',
#                                'Content-type': 'application/octet-stream',
#                                'Session-ID': upload_id,
#                                'Connection': 'keep-alive',
#                                'Content-Disposition':
# 'attachment; filename="video.mov"',
#                                'job': upload_job,
#                                'Host': 'upload.instagram.com',
#                                'User-Agent': self.USER_AGENT})
#         for i in range(0, 4):
#             start = i * request_size
#             if i == 3:
#                 end = i * request_size + lastRequestExtra
#             else:
#                 end = (i + 1) * request_size
#             length = lastRequestExtra if i == 3 else request_size
#             content_range = "bytes {start}-{end}/{lenVideo}"
# .format(start=start, end=(end - 1),
# lenVideo=len(videoData)).encode('utf-8')
#
#             self.s.headers.update({'Content-Length':
# str(end - start), 'Content-Range': content_range, })
#             response = self.s.post(upload_url,
#  data=videoData[start:start + length])
#         self.s.headers = headers
#
#         if response.status_code == 200:
#             if self.configureVideo(upload_id, video, thumbnail, caption):
#                 self.expose()
#     return False
#
# def expose(self):
#     data = json.dumps({'_uuid': self.uuid,
#                        '_uid': self.username_id,
#                        'id': self.username_id,
#                        '_csrftoken': self.token,
#                        'experiment': 'ig_android_profile_contextual_feed'})
#     return self.SendRequest('qe/expose/', self.generateSignature(data))
#
# def configure(self, upload_id, photo, caption=''):
#     (w, h) = getImageSize(photo)
#     data = json.dumps({'_csrftoken': self.token,
#                        'media_folder': 'Instagram',
#                        'source_type': 4,
#                        '_uid': self.username_id,
#                        '_uuid': self.uuid,
#                        'caption': caption,
#                        'upload_id': upload_id,
#                        'device': self.DEVICE_SETTINTS,
#                        'edits': {
#                            'crop_original_size': [w * 1.0, h * 1.0],
#                            'crop_center': [0.0, 0.0],
#                            'crop_zoom': 1.0
#                        },
#                        'extra': {
#                            'source_width': w,
#                            'source_height': h
#                        }})
#     return self.SendRequest('media/configure/?',
#  self.generateSignature(data))
#
# def configureVideo(self, upload_id, video, thumbnail, caption=''):
#     clip = VideoFileClip(video)
#     self.uploadPhoto(photo=thumbnail, caption=caption, upload_id=upload_id)
#     data = json.dumps({
#         'upload_id': upload_id,
#         'source_type': 3,
#         'poster_frame_index': 0,
#         'length': 0.00,
#         'audio_muted': False,
#         'filter_type': 0,
#         'video_result': 'deprecated',
#         'clips': {
#             'length': clip.duration,
#             'source_type': '3',
#             'camera_position': 'back',
#         },
#         'extra': {
#             'source_width': clip.size[0],
#             'source_height': clip.size[1],
#         },
#         'device': self.DEVICE_SETTINTS,
#         '_csrftoken': self.token,
#         '_uuid': self.uuid,
#         '_uid': self.username_id,
#         'caption': caption,
#     })
#     return self.SendRequest('media/configure/?video=1',
# self.generateSignature(data))
#
#


# def configureTimelineAlbum(self, media, albumInternalMetadata,
#  captionText='', location=None):
#     endpoint = 'media/configure_sidecar/'
#     albumUploadId = self.generateUploadId()
#
#     date = datetime.utcnow().isoformat()
#     childrenMetadata = []
#     for item in media:
#         itemInternalMetadata = item['internalMetadata']
#         uploadId = itemInternalMetadata.get('upload_id',
# self.generateUploadId())
#         if item.get('type', '') == 'photo':
#             # Build this item's configuration.
#             photoConfig = {'date_time_original': date,
#                            'scene_type': 1,
#                            'disable_comments': False,
#                            'upload_id': uploadId,
#                            'source_type': 0,
#                            'scene_capture_type': 'standard',
#                            'date_time_digitized': date,
#                            'geotag_enabled': False,
#                            'camera_position': 'back',
#                            'edits': {'filter_strength': 1,
#                                      'filter_name': 'IGNormalFilter'}
#                            }
#             # This usertag per-file EXTERNAL metadata
# is only supported for PHOTOS!
#             if item.get('usertags', []):
#                 # NOTE: These usertags were validated
# in Timeline::uploadAlbum.
#                 photoConfig['usertags'] =
# json.dumps({'in': item['usertags']})
#
#             childrenMetadata.append(photoConfig)
#         if item.get('type', '') == 'video':
#             # Get all of the INTERNAL per-VIDEO metadata.
#             videoDetails = itemInternalMetadata.get('video_details', {})
#             # Build this item's configuration.
#             videoConfig = {'length': videoDetails.get('duration', 1.0),
#                            'date_time_original': date,
#                            'scene_type': 1,
#                            'poster_frame_index': 0,
#                            'trim_type': 0,
#                            'disable_comments': False,
#                            'upload_id': uploadId,
#                            'source_type': 'library',
#                            'geotag_enabled': False,
#                            'edits': {
#                                'length': videoDetails.get('duration', 1.0),
#                                'cinema': 'unsupported',
#                                'original_length':
#  videoDetails.get('duration', 1.0),
#                                'source_type': 'library',
#                                'start_time': 0,
#                                'camera_position': 'unknown',
#                                'trim_type': 0}
#                            }
#
#             childrenMetadata.append(videoConfig)
#     # Build the request...
#     data = {'_csrftoken': self.token,
#             '_uid': self.username_id,
#             '_uuid': self.uuid,
#             'client_sidecar_id': albumUploadId,
#             'caption': captionText,
#             'children_metadata': childrenMetadata}
#     self.SendRequest(endpoint, self.generateSignature(json.dumps(data)))
#     response = self.LastResponse
#     if response.status_code == 200:
#         self.LastResponse = response
#         self.LastJson = json.loads(response.text)
#         return True
#     else:
#         print("Request return " + str(response.status_code) + " error!")
#         # for debugging
#         try:
#             self.LastResponse = response
#             self.LastJson = json.loads(response.text)
#         except:
#             pass
#         return False
#
# def uploadAlbum(self, media, caption=None, upload_id=None):
#     if not media:
#         raise Exception("List of media to upload can't be empty.")
#
#     if len(media) < 2 or len(media) > 10:
#         raise Exception('Instagram requires that
# albums contain 2-10 items. You tried to submit {}.'.format(len(media)))
#
#     # Figure out the media file details for ALL media in the album.
#     # NOTE: We do this first, since it validates whether the media files are
#     # valid and lets us avoid wasting time uploading totally invalid albums!
#     for idx, item in enumerate(media):
#         if not item.get('file', '') or item.get('tipe', ''):
#             raise Exception('Media at index "{}" does
#  not have the required "file" and "type" keys.'.format(idx))
#
#         # $itemInternalMetadata = new InternalMetadata();
#         # If usertags are provided, verify that the entries are valid.
#         if item.get('usertags', []):
#             self.throwIfInvalidUsertags(item['usertags'])
#
#         # Pre-process media details and throw if not allowed on Instagram.
#         if item.get('type', '') == 'photo':
#             # Determine the photo details.
#             # $itemInternalMetadata->
# setPhotoDetails(Constants::FEED_TIMELINE_ALBUM, $item['file']);
#             pass
#
#         elif item.get('type', '') == 'video':
#             # Determine the video details.
#             # $itemInternalMetadata-
# >setVideoDetails(Constants::FEED_TIMELINE_ALBUM, $item['file']);
#             pass
#
#         else:
#             raise Exception('U
# nsupported album media type "{}".'.format(item['type']))
#
#         itemInternalMetadata = {}
#         item['internalMetadata'] = itemInternalMetadata
#
#     # Perform all media file uploads.
#     for idx, item in enumerate(media):
#         itemInternalMetadata = item['internalMetadata']
#         item_upload_id = self.generateUploadId()
#         if item.get('type', '') == 'photo':
#             self.uploadPhoto(item['file'], caption=caption,
# is_sidecar=True, upload_id=item_upload_id)
#             # $itemInternalMetadata-
# >setPhotoUploadResponse($this->ig->internal-
# >uploadPhotoData(Constants::FEED_TIMELINE_ALBUM, $itemInternalMetadata));
#
#         elif item.get('type', '') == 'video':
#             # Attempt to upload the video data.
#             self.uploadVideo(item['file'], item['thumbnail'],
# caption=caption, is_sidecar=True, upload_id=item_upload_id)
#             # $itemInternalMetadata = $this->ig->internal->
# uploadVideo(Constants::FEED_TIMELINE_ALBUM, $item['file'
# ], $itemInternalMetadata);
#             # Attempt to upload the thumbnail,
# associated with our video's ID.
#             # $itemInternalMetadata->setPhotoUploadResponse
# ($this->ig->internal->uploadPhotoData(Constants::FEED_TIMEL
# INE_ALBUM, $itemInternalMetadata));
#             pass
#         item['internalMetadata']['upload_id'] = item_upload_id
#
#     albumInternalMetadata = {}
#     return self.configureTimelineAlbum(media,
# albumInternalMetadata, captionText=caption)
