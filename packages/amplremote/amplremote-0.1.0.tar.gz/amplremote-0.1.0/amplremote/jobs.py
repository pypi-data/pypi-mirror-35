from __future__ import print_function, absolute_import, division
from datetime import datetime
from flask import (
    make_response,
    abort
)

from .auth import requires_auth
from .worker import Worker

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with the API
JOBS = {}
WORKERS = {}
JOB_COUNT = len(JOBS)

def get_id():
    global JOB_COUNT
    JOB_COUNT += 1
    return str(JOB_COUNT)


@requires_auth
def read_all():
    """
    This function responds to a request for /api/jobs
    with the complete lists of jobs

    :return:        json string of list of jobs
    """
    # Create the list of jobs from our data
    return [JOBS[key] for key in sorted(JOBS.keys())]


@requires_auth
def read_one(id):
    """
    This function responds to a request for /api/jobs/{id}
    with one matching job from jobs

    :param id:   id of the job to find
    :return:        output log
    """
    # Does the job exist in jobs?
    if id in JOBS and id in WORKERS:
        job = JOBS.get(id)
        worker = WORKERS.get(id)
    else:
        abort(404, 'Job with id {id} was not found'.format(
            id=id))

    return {
        'job': job,
        'alive': worker.isAlive(),
        'output': worker.read(),
        'solution': worker.getSolution()
    }


@requires_auth
def create(job):
    """
    This function creates a new job in the jobs structure
    based on the passed in job data

    :param job:  job to create in jobs structure
    :return:        201 on success, 406 on invalid data
    """
    id = get_id()
    user = job.get('user', None)
    model = job.get('model', None)
    options = job.get('options', None)
    solver = job.get('solver', None)
    solver_options = job.get('solver_options', None)

    if model is not None and solver is not None:
        JOBS[id] = {
            'model': model,
            'id': id, 'options': options,
            'solver': solver, 'solver_options': solver_options,
            'timestamp': get_timestamp(),
        }
        WORKERS[id] = Worker(model, solver, solver_options)
        return JOBS[id], 201
    else:
        abort(406, "Must provide model and solver name for the job")


@requires_auth
def update(id, job):
    """
    This function updates an existing job in the jobs structure

    :param id:   last name of job to update in the jobs structure
    :param job:  job to update
    :return:        updated job structure
    """
    # Does the job exist in jobs?
    if id in JOBS:
        JOBS[id]['user'] = job.get('user')
        JOBS[id]['timestamp'] = get_timestamp()
        return JOBS[id]

    # otherwise, nope, that's an error
    else:
        abort(404, 'Job with id {id} not found'.format(id=id))


@requires_auth
def delete(id):
    """
    This function deletes a job from the jobs structure

    :param id:   id of the job to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the job to delete exist?
    if id in JOBS:
        del JOBS[id]
        del WORKER[id]
        return make_response('{id} successfully deleted'.format(id=id), 200)

    # Otherwise, nope, job to delete not found
    else:
        abort(404, 'Job with id {id} not found'.format(id=id))
