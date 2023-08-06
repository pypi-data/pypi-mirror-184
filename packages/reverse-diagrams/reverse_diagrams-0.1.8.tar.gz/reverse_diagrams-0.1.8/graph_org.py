
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit

with Diagram("Organizations-State", show=False, direction="TB"):
    ou = OrganizationsOrganizationalUnit("OU")
    oa = OrganizationsAccount("Account")

    with Cluster('Organizations'):

        oo = Organizations('o-gw1gom4vd7\n634252486409\nr-2uoz')

        ou_Bank4usRCI= OrganizationsOrganizationalUnit("ou-2uoz-ysgn3x7o\nBank4usRCI")

        oo>> ou_Bank4usRCI

        ou_ProductsSecurity= OrganizationsOrganizationalUnit("ou-2uoz-y8ozr53i\nProductsSecurity")

        oo>> ou_ProductsSecurity

        ou_DevSecOps= OrganizationsOrganizationalUnit("ou-2uoz-igncnk1m\nDevSecOps")

        oo>> ou_DevSecOps

        ou_Suspended= OrganizationsOrganizationalUnit("ou-2uoz-wn4jcrya\nSuspended")

        oo>> ou_Suspended

        ou_Infrastructure= OrganizationsOrganizationalUnit("ou-2uoz-t49i8js2\nInfrastructure")

        oo>> ou_Infrastructure

        ou_WorkLoadsRCI= OrganizationsOrganizationalUnit("ou-2uoz-qsot2f01\nWorkLoadsRCI")

        ou_Bank4usRCI>> ou_WorkLoadsRCI

        ou_InfrastructureRCI= OrganizationsOrganizationalUnit("ou-2uoz-wer9cp68\nInfrastructureRCI")

        ou_Bank4usRCI>> ou_InfrastructureRCI

        ou_PlayGroundRCI= OrganizationsOrganizationalUnit("ou-2uoz-y42c2jx1\nPlayGroundRCI")

        ou_Bank4usRCI>> ou_PlayGroundRCI

        ou_WorkLoadsRCI>> OrganizationsAccount("925371814738\naws-qa-bank4us-p\nroduct-sophos")

        oo >> OrganizationsAccount("634252486409\ncloud-saas@sophossolutions.com")

        ou_InfrastructureRCI>> OrganizationsAccount("318253146201\naws-shared-bank4\nus-product-sophos")

        ou_PlayGroundRCI>> OrganizationsAccount("450073187267\naws-test-product\n-sophos")

        ou_ProductsSecurity>> OrganizationsAccount("675404175100\naws-security-pro\nduct-sophos")

        ou_ProductsSecurity>> OrganizationsAccount("714892466397\naws-logsbackups-\nproduct-sophos")

        ou_DevSecOps>> OrganizationsAccount("124962754109\naws-devsecops-pr\noduct-sophos")

        ou_WorkLoadsRCI>> OrganizationsAccount("151377982441\naws-dev-bank4us-\nproduct-sophos")

        ou_InfrastructureRCI>> OrganizationsAccount("753541840841\naws-networking-b\nank4us-products-sophos")

        ou_Infrastructure>> OrganizationsAccount("818468602340\naws-networking-p\nroduct-sophos")

        ou_WorkLoadsRCI>> OrganizationsAccount("872865219972\naws-prod-bank4us\n-product-sophos")

        ou_Infrastructure>> OrganizationsAccount("570700223503\naws-shared-produ\nct-sophos")
