
The Elegant Quine
Self Replicating Python Code
Keep in mind to truly be a quine, it cannot be executed outside a python shell, otherwise the input is not outputting a copy


	s='s=%r;print(s%%s)';print(s%s)
