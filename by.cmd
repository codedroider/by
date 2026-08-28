:: "by" by codedroider.github.io
@set "arg=%~1"
@if defined arg (
  @echo script by %arg%
) else (
  @echo argument is null!
)
