// .prettierrc.cjs
module.exports = {
  // 每个缩进级别使用 4 个空格
  tabWidth: 4,
  // 一行代码的最大字符数，超过则换行
  printWidth: 120,
  // 不使用 Tab 字符缩进，使用空格
  useTabs: false,
  // 对象/函数的括号与第一行内容放在同一行
  bracketSameLine: true,
  // 对象字面量的括号内不添加空格
  bracketSpacing: false,
  // 根据文件当前行尾符自动处理
  endOfLine: "auto",

  // 插件配置
  plugins: ["prettier-plugin-multiline-arrays"],
  // 数组元素超过 1 个时强制换行
  multilineArraysWrapThreshold: 1,

  // 针对特定文件类型的覆盖配置
  overrides: [
    {
      // YAML 文件配置
      files: ["**/*.yml", "**/*.yaml"],
      options: {
        parser: "yaml",
        tabWidth: 2, // YAML 专用缩进
      },
    },
    {
      // JSON 文件配置
      files: ["*.json"],
      options: {
        // parser: "json",
        parser: "json5", // 使用 json5 解析器支持注释
        useTabs: true, // JSON 专用缩进
        bracketSameLine: false,
      },
    },
  ],
};
