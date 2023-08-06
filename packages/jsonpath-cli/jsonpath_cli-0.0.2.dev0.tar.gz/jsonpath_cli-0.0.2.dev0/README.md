
# The **jsonpath_cli** Package.

The **jsonpath_cli** is an extension to [jsonpath_tp](https://pypi.org/project/jsonpath-tp/) implementation built on 
top of [treepath](https://pypi.org/project/treepath/) technology. 



# Quick Start Command Line Interface
To use the cli install the jsonpath_cli python package in a venv:
```
python -m venv venv
source bin venv/bin/activate
pip install jsonpath_cli
```

A jsonpath example that gets  c's value from json data.
jsonpath "$.star.planets.inner[?(@.name=='Earth')].name" tests/data/solar-system.json
> "Earth"


# Solar System Json Document

The examples shown in this README use the following json document.  It describes our solar system. Click to expand.  
<details><summary>solar_system = {...}</summary>
<p>

```json

{
  "star": {
    "name": "Sun",
    "diameter": 1391016,
    "age": null,
    "planets": {
      "inner": [
        {
          "name": "Mercury",
          "Number of Moons": "0",
          "diameter": 4879,
          "has-moons": false
        },
        {
          "name": "Venus",
          "Number of Moons": "0",
          "diameter": 12104,
          "has-moons": false
        },
        {
          "name": "Earth",
          "Number of Moons": "1",
          "diameter": 12756,
          "has-moons": true
        },
        {
          "name": "Mars",
          "Number of Moons": "2",
          "diameter": 6792,
          "has-moons": true
        }
      ],
      "outer": [
        {
          "name": "Jupiter",
          "Number of Moons": "79",
          "diameter": 142984,
          "has-moons": true
        },
        {
          "name": "Saturn",
          "Number of Moons": "82",
          "diameter": 120536,
          "has-moons": true
        },
        {
          "name": "Uranus",
          "Number of Moons": "27",
          "diameter": 51118,
          "has-moons": true
        },
        {
          "name": "Neptune",
          "Number of Moons": "14",
          "diameter": 49528,
          "has-moons": true
        }
      ]
    }
  }
}


```

</p>
</details>

