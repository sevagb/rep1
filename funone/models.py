from django.db import models

# Create your models here.

class VaultContract(models.Model):
	deal_id = models.CharField(primary_key=True, max_length=40, db_column='UNIVERSAL_APP_ID')
	lender_id = models.CharField(max_length=3, db_column='LENDER_ID')
	lender_app_id = models.CharField(max_length=30, db_column='LENDER_APP_ID')
	status = models.CharField(max_length=40, db_column='CONTRACT_STATUS')
	tran_sid = models.IntegerField(db_column='EEBS_SID')
	dp_sid = models.IntegerField(db_column='EEBS_DP_SID')
	vin = models.CharField(max_length=17, db_column='VIN_NUM')
	
	class Meta:
		managed = False
		db_table = 'ECONTRACT_VAULT'