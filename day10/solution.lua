-- a is a sorted list of input values (with 0 added to the start and biggest value +3 at the end)
local ans = 1
local ones = 0
for i=1,#a-1 do
    if (a[i+1] - a[i]) == 1 then
        ones = ones + 1
    else
        if ones > 1 then
            if ones == 2 then
                ans = ans * 2
            elseif ones == 3 then
                ans = ans * 4
            elseif ones == 4 then
                ans = ans * 7
            end
        end
        ones = 0
    end
end
print("ans:", ans)
