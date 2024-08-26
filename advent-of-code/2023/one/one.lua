function dump(o)
  if type(o) == "table" then
    local s = "{ "
    for k, v in pairs(o) do
      if type(k) ~= "number" then
        k = '"' .. k .. '"'
      end
      s = s .. "[" .. k .. "] = " .. dump(v) .. ","
    end
    return s .. "} "
  else
    return tostring(o)
  end
end

function find_number(text)
  local numbers = {}
  for num in text:gmatch("%d") do
    table.insert(numbers, num)
  end

  local first_number = 0
  local second_number = 0
  if #numbers > 1 then
    first_number = numbers[1]
    second_number = numbers[#numbers]
  else
    first_number = numbers[1]
    second_number = numbers[1]
  end
  return tonumber(first_number .. second_number)
end

function main(file_name)
  local file = io.open(file_name, "r")
  local sum = 0

  if not file then
    return
  end

  for line in file:lines() do
    local numbers = find_number(line)
    sum = sum + numbers
  end
  file:close()
  return sum
end

-- pass the file name as command line argument
if arg[1] then
  local sum = main(arg[1])
  print(sum)
  return
end
