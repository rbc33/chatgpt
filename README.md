# chatgpt

# oauth - Python Oauth2 - login with Google - Stack Overflow  https://stackoverflow.com/questions/10271110/python-oauth2-login-with-google
chatgpt % python  gpt3-5.py
Traceback (most recent call last):
  File "/Users/user/pypro/chatgpt/gpt3-5.py", line 15, in <module>
    completion = openai.ChatCompletion.create(
  File "/Users/user/pypro/chatgpt/venv/lib/python3.9/site-packages/openai/api_resources/chat_completion.py", line 25, in create
    return super().create(*args, **kwargs)
  File "/Users/user/pypro/chatgpt/venv/lib/python3.9/site-packages/openai/api_resources/abstract/engine_api_resource.py", line 153, in create
    response, _, api_key = requestor.request(
  File "/Users/user/pypro/chatgpt/venv/lib/python3.9/site-packages/openai/api_requestor.py", line 298, in request
    resp, got_stream = self._interpret_response(result, stream)
  File "/Users/user/pypro/chatgpt/venv/lib/python3.9/site-packages/openai/api_requestor.py", line 700, in _interpret_response
    self._interpret_response_line(
  File "/Users/user/pypro/chatgpt/venv/lib/python3.9/site-packages/openai/api_requestor.py", line 763, in _interpret_response_line
    raise self.handle_error_response(
openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.
