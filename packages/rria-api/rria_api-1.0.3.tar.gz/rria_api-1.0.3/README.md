# RRIA-API

The `rria-api` is an easy-to-use package that provides a common interface to control robots used by the Residence in Robotics
and AI at the UFPE's informatics center. The API currently supports the use of Kinova Gen3 lite and Niryo NED, with
plans to support a Denso robot.

### **Requirements**

- Python 3.9+
- Kortex API .whl package

### **Instalation**
1. Download the v2.3.0 Kortex API .whl package (required for controlling the Kinova Gen3 and Gen3 lite):

- [kortex_api-2.3.0.post34-py3-none-any.whl](https://artifactory.kinovaapps.com/ui/native/generic-public/kortex/API/2.3.0/kortex_api-2.3.0.post34-py3-none-any.whl).

2. Install the downloaded package with `pip`:

```
$ pip install <path to kortex_api-2.3.0.post34-py3-none-any.whl>
```

3. Install the latest `rria-api` package with `pip`:

```
$ pip install rria-api
```