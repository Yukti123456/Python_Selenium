# 25. Nested Data Pattern Matching — Challenge
#
# Given:
#
# user = {
#     "name": "Yukti",
#     "role": "tester",
#     "status": "active"
# }
#
# Use match-case to identify:
#
# Active tester
# Inactive tester
# Active admin
# Inactive admin
#
# Handle other combinations with a wildcard case.
user = {
    "name": "Yukti",
    "role": "tester",
    "status": "active"
}

match user:
    case _ if (user["name"] != "admin" and user["status"] == "active"):
        print("Active tester")
    case _ if (user["name"] != "admin" and user["status"] == "Inactive"):
        print("Inactive tester")
    case _ if (user["name"] == "admin" and user["status"] == "active"):
        print("Active Admin")
    case _ if (user["name"] == "admin" and user["status"] == "Inactive"):
        print("Inactive Admin")
