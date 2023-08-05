from user_query_optimizer import get_optimizer
import json
from redash import models
from redash.handlers import api
from redash.handlers.base import BaseResource, get_object_or_404
from redash.permissions import require_access, view_only
from redash.query_runner import BaseQueryRunner
from redash.query_runner.pg import PostgreSQL

class OptimizerResource(BaseResource):
    def optimize(self, query_id):
        query = get_object_or_404(models.Query.get_by_id_and_org, query_id, self.current_org)
        query_text = query.query_text
        # schema = something
        # db = something
        schema = {"partitions" : ["submission_date_s3", "app_name", "os"]}
        optimizer = get_optimizer("presto", schema)
        hints = optimizer.optimize_query(query_text)
        return hints


def optimizer_endpoint(app=None):
	BaseQueryRunner.optimize = optimize
	api.add_org_resource(OptimizerResource, '/api/queries/<query_id>/optimize', endpoint='optimizer_endpoint')
