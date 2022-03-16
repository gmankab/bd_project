import bd

bd.install_libs(
    requirements = ['requests'],
    zip_name = 'project_libs.zip',
)

import requests

# def pp():
#     print(
#         bd.Path(
#             f'{pathlib.Path(__file__).parent}'
#         ).tree(
#             ignore = ['__pycache__'],
#             md_diff = True,
#         )
#     )
# pp()
