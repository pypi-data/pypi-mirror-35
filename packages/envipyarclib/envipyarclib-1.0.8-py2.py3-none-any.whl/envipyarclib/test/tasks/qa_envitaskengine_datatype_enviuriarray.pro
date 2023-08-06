;+
; :Description:
;    Task to test task engine ENVIURIARRAY datatype
;    See qa_envitaskengine_datatype_enviuriarray.task for details
;
; :Author:
;    JWD, July, 2018 - Initial Draft
;-
pro qa_envitaskengine_datatype_enviuriarray, $
  INPUT=input, $
  OUTPUT=output
  compile_opt idl2
  
  if (Isa(input, /SCALAR)) then begin
    Message, 'INPUT is a scalar'
  endif

  if (~Isa(input, /ARRAY)) then begin
    Message, 'INPUT is not an array'
  endif

  if (Isa(input, 'Collection')) then begin
    Message, 'INPUT is a collection and should not be'
  endif

  output = input
end
