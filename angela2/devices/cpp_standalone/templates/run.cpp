{% macro cpp_file() %}
#include<stdlib.h>
#include "objects.h"
#include<ctime>
#include "randomkit.h"

{% for codeobj in code_objects | sort(attribute='name') %}
#include "code_objects/{{codeobj.name}}.h"
{% endfor %}

{% for name in user_headers | sort %}
#include {{name}}
{% endfor %}

void angela_start()
{
	_init_arrays();
	_load_arrays();
	// Initialize clocks (link timestep and dt to the respective arrays)
    {% for clock in clocks | sort(attribute='name') %}
    angela::{{clock.name}}.timestep = angela::{{array_specs[clock.variables['timestep']]}};
    angela::{{clock.name}}.dt = angela::{{array_specs[clock.variables['dt']]}};
    angela::{{clock.name}}.t = angela::{{array_specs[clock.variables['t']]}};
    {% endfor %}
    for (int i=0; i<{{openmp_pragma('get_num_threads')}}; i++)
	    rk_randomseed(angela::_mersenne_twister_states[i]);  // Note that this seed can be potentially replaced in main.cpp
}

void angela_end()
{
	_write_arrays();
	_dealloc_arrays();
}

{% for name, lines in run_funcs.items() | sort(attribute='name') %}
void {{name}}()
{
	using namespace angela;

    {{lines|autoindent}}
}

{% endfor %}

{% endmacro %}

/////////////////////////////////////////////////////////////////////////////////////////////////////

{% macro h_file() %}

void angela_start();
void angela_end();

{% for name, lines in run_funcs.items() | sort(attribute='name') %}
void {{name}}();
{% endfor %}

{% endmacro %}
