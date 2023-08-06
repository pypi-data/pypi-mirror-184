NAMESPACE={{ namespace|default("clusters") if hypershift|default(False) else 'openshift-config' }}
{% if hypershift|default(False) %}
oc patch hc -n $NAMESPACE $CLUSTER -p='[{"op": "remove", "path": "/spec/configuration/oauth/identityProviders"}]' --type=json
{% else %}
oc patch oauth cluster -p='[{"op": "remove", "path": "/spec/identityProviders"}]' --type=json
{% endif %}
oc delete secret htpass-secret -n $NAMESPACE
