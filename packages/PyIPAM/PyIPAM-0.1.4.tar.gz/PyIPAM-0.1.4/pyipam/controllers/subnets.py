#!/usr/bin/python
from pyipam.server import app
from flask import flash, redirect, render_template, send_from_directory, url_for, request, session, abort
from pyipam.models.subnets import SubnetsModel

subnetsModel = SubnetsModel()

@app.route('/subnet/add', methods=['GET', 'POST'])
def subnet_add():
    btn_text = "Add Subnet"
    if request.method == 'POST':
        fields={
            'subnet': request.form['subnet'],
            'vlan': request.form['vlan'],
            'description': request.form['description']
        }
        if (subnetsModel.add_subnet(fields)):
            return "<script>window.close()</script>"
        else:
            return render_template(
                'subnet/form.html',
                btn_text=btn_text,
                error=True,
                error_message="Subnet already exists."
            )
    elif request.method == 'GET':
        return render_template(
            'subnet/form.html', 
            btn_text=btn_text
        )

@app.route('/subnet/edit/<string:id>/', methods=['GET', 'POST'])
def subnet_edit(id):
    btn_text = "Save Subnet"
    subnet = subnetsModel.load_subnet(id)
    if (request.method == 'POST'):
        fields={
            'subnet': request.form['subnet'],
            'vlan': request.form['vlan'],
            'description': request.form['description']
        }
        subnetsModel.edit_subnet(id, fields)
        return "<script>window.close()</script>"
    elif request.method == 'GET':
        return render_template(
            'subnet/form.html', 
            btn_text=btn_text,
            subnet=subnet
        )

@app.route('/subnet/delete/<string:id>/', methods=['GET'])
def subnet_delete(id):
    subnetsModel.delete_subnet(id)
    return redirect('/')

@app.route('/subnet/view/<string:subnet_id>/', methods=['GET'])
def subnet_view(subnet_id):
    if (request.method == 'GET'):
        if (subnet_id):
            subnet = subnetsModel.load_subnet(subnet_id)
            ip_addresses = subnetsModel.load_ip_addresses(subnet_id)
            last_id = subnetsModel.load_last_id(subnet_id)
            last_id = int(last_id[0][0] - 1)

        if (request.args.get('page')):
            if (int(request.args.get('page')) > 1): 
                row_start_num = int(request.args.get('page')) * 100
                row_finish_num = row_start_num * 2
            else:
                row_start_num = 0  
                row_finish_num = 100
        else:
            row_start_num = 0
            row_finish_num = 100

        return render_template(
            '/subnet/view.html',
            subnet=subnet,
            row_start_num=row_start_num,
            row_finish_num=row_finish_num,
            last_id=last_id,
            ip_addresses=ip_addresses
        )

@app.route('/subnet/update/<string:subnet_id>/', methods=['GET', 'POST'])
def subnet_ip_update(subnet_id):
    if request.method == 'POST':
        json = request.get_json()
        subnetsModel.save_ip_address(subnet_id, json.get('id'), json.get('field'), json.get('value'))
        return 'Data posted:'
    else:
        return redirect('/subnet/view/' + subnet_id + '/page/1/')

@app.route('/subnet/ip/scan/<string:subnet_id>/<string:ip_id>/', methods=['GET'])
def subnet_ip_scan(subnet_id, ip_id):
    if (subnet_id and ip_id):
        ip = subnetsModel.load_ip_address(subnet_id, ip_id)
        subnetsModel.scan_ip(subnet_id, ip[0][1])
        return redirect('/subnet/view/' + subnet_id)