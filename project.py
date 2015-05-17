from project_module import project_object, image_object, link_object, challenge_object

p = project_object('project_management', 'Project management')
p.domain = 'http://www.aidansean.com/'
p.path = ''
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.folder_name = 'Other'
p.github_repo_name = 'project_management'
p.mathjax = True
p.links.append(link_object(p.domain, 'projects', 'Blog'))
p.introduction = 'This project was made to manage other projects.  Each project has its own metadata which is parsed and arranged to give a useful summary of what the project does, how it was developed, and what I learned during development.'
p.overview = '''Each project has a python script that summarises the metadata, including the GitHub repository, the relevant links, a short description of the project, and details of implementation.  Summaries are made for the <a href="/projects/">Projects Wordpress blog</a>, and special links made for the PHP pages for projects that are hosted on my website.  The scripts are organised so that they iterate over all projects (currently 83 and growing) at once, allowing a summary of all projects to be formulated.

This project management will eventually be extended to include icons, images, and other useful information.  So far this has mostly be used to allow me to catalogue my existing projects in my spare time, which has taken ~15 months, but now that is nearly complete my needs will change, so I will add new functionalities.'''

p.challenges.append(challenge_object('This project needs to be versatile enough to handle a lot metadata about many projects.', 'In order to accommodate so many projects I had to create a new top level directory in my user space which is arranged hierarchically by category to contain all the projects.  The choice to use python is motivated by the need to have a project management system that is versatile enough to handle a wide divrersity of projects with different metadata.', 'Resolved.'))


