# ok: eval-exec
eval("1 + 1")

# ruleid: eval-exec
eval(user_input)

# ok: eval-exec
exec("1 + 1")

# ruleid: eval-exec
exec(user_input)

i = "1 + 1"
# ok: eval-exec
eval(i)

# ok: eval-exec
exec(i)

j = user_input
# ruleid: eval-exec
eval(j)

# ruleid: eval-exec
exec(j)

k = i
# ok: eval-exec
eval(k)

# ok: eval-exec
exec(k)
