local function latex_escape(text)
  local replacements = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["$"] = "\\$",
    ["&"] = "\\&",
    ["#"] = "\\#",
    ["_"] = "\\_",
    ["%"] = "\\%",
    ["~"] = "\\textasciitilde{}",
    ["^"] = "\\textasciicircum{}",
  }

  return text:gsub("[\\{}$&#_%%~^]", replacements)
end

local function has_class(classes, target)
  for _, class in ipairs(classes) do
    if class == target then
      return true
    end
  end
  return false
end

local function prepend_title(blocks, title)
  local output = { pandoc.Para({ pandoc.Strong({ pandoc.Str(title) }) }) }
  for _, block in ipairs(blocks) do
    output[#output + 1] = block
  end
  return output
end

function Div(div)
  if not has_class(div.classes, "worked-example") then
    return nil
  end

  local title = div.attributes.title or "Worked Example"

  if FORMAT:match("latex") then
    local blocks = {
      pandoc.RawBlock("latex", "\\begin{workedexample}{" .. latex_escape(title) .. "}"),
    }
    for _, block in ipairs(div.content) do
      blocks[#blocks + 1] = block
    end
    blocks[#blocks + 1] = pandoc.RawBlock("latex", "\\end{workedexample}")
    return blocks
  end

  return prepend_title(div.content, title)
end

function Para(para)
  if #para.content ~= 1 or para.content[1].t ~= "Strong" then
    return nil
  end

  local caption = pandoc.utils.stringify(para.content[1])
  if not caption:match("^Table%s+%d+%.%d+:") then
    return nil
  end

  if FORMAT:match("latex") then
    return pandoc.RawBlock("latex", "\\booktablecaption{" .. latex_escape(caption) .. "}")
  end

  return para
end
