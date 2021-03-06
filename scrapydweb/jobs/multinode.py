# coding: utf8
from flask import url_for, render_template

from ..myview import MyView


class MultinodeView(MyView):
    methods = ['POST']

    def __init__(self):
        super(self.__class__, self).__init__()

        self.opt = self.view_args['opt']
        self.project = self.view_args['project']
        self.version_job = self.view_args['version_job']

        self.template = 'scrapydweb/multinode_results.html'

    def dispatch_request(self, **kwargs):
        selected_nodes = self.get_selected_nodes()
        url_xhr = url_for('api', node=selected_nodes[0], opt=self.opt,
                          project=self.project, version_spider_job=self.version_job)

        if self.opt == 'stop':
            title = "Stop Job (%s) of Project (%s)" % (self.project, self.version_job)
            url_overview = url_for('overview', node=self.node, opt='listjobs', project=self.project)
        elif self.opt == 'delversion':
            title = "Delete Version (%s) of Project (%s)" % (self.version_job, self.project)
            url_overview = url_for('overview', node=self.node, opt='listversions', project=self.project)
        else:  # elif opt == 'delproject':
            title = "Delete Project (%s)" % self.project
            url_overview = url_for('overview', node=self.node, opt='listprojects', project=self.project)

        kwargs = dict(
            node=self.node,
            opt=self.opt,
            project=self.project,
            version_job=self.version_job,
            selected_nodes=selected_nodes,
            url_xhr=url_xhr,
            title=title,
            url_overview=url_overview
        )
        return render_template(self.template, **kwargs)
