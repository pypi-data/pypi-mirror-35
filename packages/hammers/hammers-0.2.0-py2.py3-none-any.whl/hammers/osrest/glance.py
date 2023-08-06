"""
Glance API shims. See `Glance HTTP API
<https://developer.openstack.org/api-ref/image/v2/index.html>`_
"""

import requests
import textwrap


def images(auth, query=None):
    """
    Retrieves all images, filtered by `query`, if provided.

    Doesn't support pagination. Don't request too many.

    For querying, accepts a dictionary. If the value is a non-string iterable,
    the key is repeated in the query with each element in the iterable.
    """
    response = requests.get(
        url=auth.endpoint('image') + '/v2/images',# + query,
        params=query,
        headers={'X-Auth-Token': auth.token},
    )
    response.raise_for_status()

    images = response.json()['images']
    return images


def image(auth, id=None, name=None):
    """
    Looks up image by `id` or `name`. If `name` is not unique given the scope
    of authentication (e.g. private image owned by someone else may be hidden),
    an error is raised.
    """
    if id is None and name is None:
        raise ValueError('must specify name or id')
    if id is None:
        matches = images(auth, query={'name': name})
        if len(matches) < 1:
            raise RuntimeError('no images found with name "{}"'.format(name))
        elif len(matches) > 1:
            raise RuntimeError('multiple images ({}) found with name "{}"'.format(len(matches), name))
        id = matches[0]['id']

    response = requests.get(
        url=auth.endpoint('image') + '/v2/images/{}'.format(id),
        headers={'X-Auth-Token': auth.token},
    )
    response.raise_for_status()

    image = response.json()
    return image


# def image_create(auth, name, *, disk_format='qcow2', container_format='bare', visibility='private', extra=None):
# <py2 kwargs compat>
def image_create(auth, name, **kwargs):
    """Creates empty image entry, ready to be filled by an upload command.

    If provided, `extra` is a mapping to set custom properties."""
    disk_format = kwargs.get('disk_format', 'qcow2')
    container_format = kwargs.get('container_format', 'bare')
    visibility = kwargs.get('visibility', 'private')
    extra = kwargs.get('extra', None)
# </py2 kwargs compat>
    if extra is None:
        extra = {}

    data = {
        'name': name,
        'disk_format': disk_format,
        'container_format': container_format,
        'visibility': visibility,
        # **extra,
    }
    data.update(extra)
    response = requests.post(
        url=auth.endpoint('image') + '/v2/images',
        headers={
            'X-Auth-Token': auth.token,
        },
        json=data,
    )
    response.raise_for_status()
    return response.json()


def image_delete(auth, id):
    """Deletes image by ID"""
    response = requests.delete(
        url=auth.endpoint('image') + '/v2/images/{}'.format(id),
        headers={
            'X-Auth-Token': auth.token,
        },
    )
    response.raise_for_status()
    return response


def image_tag(auth, id, tag):
    response = requests.put(
        url=auth.endpoint('image') + '/v2/images/{}/tags/{}'.format(id, tag),
        headers={'X-Auth-Token': auth.token},
    )
    response.raise_for_status()


def image_untag(auth, id, tag):
    response = requests.delete(
        url=auth.endpoint('image') + '/v2/images/{}/tags/{}'.format(id, tag),
        headers={'X-Auth-Token': auth.token},
    )
    response.raise_for_status()


#def image_properties(auth, id, *, add=None, remove=None, replace=None):
# <py2 kwargs compat>
def image_properties(auth, id, **kwargs):
    """
    Add/remove/replace properties on the image. Some standard properties can
    be modified (name, visibility), some can't (id, checksum), but custom
    fields can be whatever.

    :param mapping add:     properties to add
    :param iterable remove: properties to delete
    :param mapping replace: properties to replace by key
    """
    add = kwargs.get('add', None)
    remove = kwargs.get('remove', None)
    replace = kwargs.get('replace', None)
# </py2 kwargs compat>
    patch = []
    if add is not None:
        for key, value in add.items():
            patch.append({'op': 'add', 'path': '/{}'.format(key), 'value': value})
    if remove is not None:
        for key in remove:
            patch.append({'op': 'remove', 'path': '/{}'.format(key)})
    if replace is not None:
        for key, value in replace.items():
            patch.append({'op': 'replace', 'path': '/{}'.format(key), 'value': value})

    response = requests.patch(
        url=auth.endpoint('image') + '/v2/images/{}'.format(id),
        headers={
            'X-Auth-Token': auth.token,
            'Content-Type': 'application/openstack-images-v2.1-json-patch', # subset of full JSON patch
        },
        json=patch,
    )
    response.raise_for_status()
    return response.json()


def image_upload_curl(auth, id, filepath):
    """Generates an cURL command to upload an image file at `filepath` to be
    associated with the Glance image. Includes authentication header, so
    is stateless and can be run most anywhere."""
    return textwrap.dedent('''\
    curl -i -X PUT -H "X-Auth-Token: {token}" \
        -H "Content-Type: application/octet-stream" \
        --data-binary @"{filepath}" \
        {url}'''.format(
        token=auth.token,
        filepath=filepath,
        url=auth.endpoint('image') + '/v2/images/{}/file'.format(id),
    ))


def image_download_curl(auth, id, filepath=None):
    """Generates a cURL command to download an image file to `filepath`.
    If `filepath` is not provided, dumps to ``~/<image name>.img``. The
    request is authenticated, so can be run most anywhere."""
    if filepath is None:
        image = glance_image(auth, id)
        filepath = '~/{}.img'.format(image['name'])

    return textwrap.dedent('''\
    curl -D /dev/stdout -X GET -H "X-Auth-Token: {token}" \
        {url} \
        -o {filepath}'''.format(
        token=auth.token,
        url=auth.endpoint('image') + '/v2/images/{}/file'.format(id),
        filepath=filepath,
    ))


# backwards compatible, hack-namespaced.
__all__ = [
    'glance_images',
    'glance_image',
    'glance_image_create',
    'glance_image_delete',
    'glance_image_tag',
    'glance_image_untag',
    'glance_image_properties',
    'glance_image_upload_curl',
    'glance_image_download_curl',
]

glance_images = images
glance_image = image
glance_image_create = image_create
glance_image_delete = image_delete
glance_image_tag = image_tag
glance_image_untag = image_untag
glance_image_properties = image_properties
glance_image_upload_curl = image_upload_curl
glance_image_download_curl = image_download_curl
