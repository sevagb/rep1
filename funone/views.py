#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from funone.models import VaultContract
from django.template import loader
import requests, json
#from funone.models import Page

def index(request):
	return HttpResponse("Python and Django are fun ...")
	
def digicon(request, dealid):
	con = VaultContract.objects.get(deal_id=dealid)
	strOut = "<h1>Your contract data</h1><br />Deal ID: " + con.deal_id
	strOut += "<br />Lender ID: " + con.lender_id
	strOut += "<br />Lender App ID: " + con.lender_app_id
	strOut += "<br />Status: " + con.status
	strOut += "<br />Tran Sid: " + str(con.tran_sid)
	strOut += "<br />Doc Profile Sid: " + str(con.dp_sid)
	strOut += "<br />VIN: " + con.vin
	return HttpResponse(strOut)
	
def ecoreorgcreate(request):
	if request.method == 'POST':
		orgname = request.POST.get('txtorgname')
		fullname = request.POST.get('txtlegalname')
		street = request.POST.get('txtstreet')
		city = request.POST.get('txtcity')
		state = request.POST.get('txtstate')
		zip = request.POST.get('txtszip')
		buf = request.POST.get('txtretbuf')
		
		VAULT_SVC_EP = "http://10.117.36.46:6118/vault/econtractvault.svc/ecore-admin/orgs"
		
		payload = { "org_name": orgname, "full_name": fullname, "street": street,
		"city": city, "state": state, "country": "USA", "zip": zip, "user": "123456",
		"retention_buffer": buf }
		
		headers = {'content-type': 'application/json'}
		
		r = requests.post(VAULT_SVC_EP, data=json.dumps(payload), headers=headers)
		
		if r.status_code == 201:
			return(HttpResponse("Vault org " + fullname + " created"))
		
		return(HttpResponse("Error creating vault org - status code: " + str(r.status_code)))
	
	frm = loader.get_template('forms/ecoreorgcreate.html')
	return HttpResponse(frm.render({}, request))
	