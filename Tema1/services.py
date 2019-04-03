import apis.developer_here_api
import apis.ip_api
import apis.publicapis_api
import apis.ipify_api

routing_service = apis.developer_here_api.RoutingService()
ipgeolocation_service = apis.ip_api.GeolocationService()
apis_service = apis.publicapis_api.APIsService()
public_ip_service = apis.ipify_api.PublicIPService()