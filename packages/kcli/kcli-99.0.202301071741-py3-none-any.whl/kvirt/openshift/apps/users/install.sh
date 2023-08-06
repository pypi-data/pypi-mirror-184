DEV_USER={{ users_dev }}
DEV_PASSWORD={{ users_devpassword }}
ADMIN_USER={{ users_admin }}
ADMIN_PASSWORD={{ users_adminpassword }}
echo "Adding dev user $DEV_USER with password $DEV_PASSWORD"
echo "Adding admin user $ADMIN_USER with password $ADMIN_PASSWORD"
printf "$ADMIN_USER:$(openssl passwd -apr1 $ADMIN_PASSWORD )\n$DEV_USER:$(openssl passwd -apr1 $DEV_PASSWORD )\n" > htpasswd
NAMESPACE={{ namespace|default("clusters") if hypershift|default(False) else 'openshift-config' }}
oc create secret generic htpass-secret --from-file=htpasswd=htpasswd -n $NAMESPACE
{% if hypershift|default(False) %}
CLUSTER= {{ cluster }}
oc patch hc -n $NAMESPACE $CLUSTER ci-hypershift --patch-file oauth_hypershift.yml --dry-run=client -o yaml | oc replace -f - -n $NAMESPACE $CLUSTER
{% else %}
oc apply -f oauth.yml
{% endif %}
echo "Granting cluster-admin role to $ADMIN_USER"
oc adm policy add-cluster-role-to-user cluster-admin $ADMIN_USER
