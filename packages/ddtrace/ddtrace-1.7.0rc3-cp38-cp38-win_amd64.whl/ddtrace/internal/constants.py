PROPAGATION_STYLE_DATADOG = "datadog"
PROPAGATION_STYLE_B3 = "b3multi"
PROPAGATION_STYLE_B3_SINGLE_HEADER = "b3 single header"
_PROPAGATION_STYLE_W3C_TRACECONTEXT = "tracecontext"
_PROPAGATION_STYLE_NONE = "none"
_PROPAGATION_STYLE_DEFAULT = "tracecontext,datadog"
PROPAGATION_STYLE_ALL = (
    _PROPAGATION_STYLE_W3C_TRACECONTEXT,
    PROPAGATION_STYLE_DATADOG,
    PROPAGATION_STYLE_B3,
    PROPAGATION_STYLE_B3_SINGLE_HEADER,
    _PROPAGATION_STYLE_NONE,
)
W3C_TRACESTATE_KEY = "tracestate"
W3C_TRACEPARENT_KEY = "traceparent"
W3C_TRACESTATE_ORIGIN_KEY = "o"
W3C_TRACESTATE_SAMPLING_PRIORITY_KEY = "s"
DEFAULT_SERVICE_NAME = "unnamed_python_service"
