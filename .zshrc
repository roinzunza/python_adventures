# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"
#ZSH_THEME=""
ZSH_THEME="robbyrussell"
export PATH=$PATH:$HOME/go/bin


plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch $(uname -m)"

export ZPLUG_HOME=/opt/homebrew/opt/zplug
source $ZPLUG_HOME/init.zsh

#zplug "mafredri/zsh-async", from:github

#plug "sindresorhus/pure", use:pure.zsh, from:github, as:theme
#zplug load

# Install plugins if there are plugins that have not been installed
#if ! zplug check --verbose; then
#    printf "Install? [y/N]: "
#    if read -q; then
#        echo; zplug install
#    fi
#fi
# Iterm things
function tabdefault()
{
    tabtitle
    tabcolor default
}

function tabtitle()
{
    TABTITLE="${1:- }"

    echo -en '\ek'${TABTITLE}'\e\\'
}

function tabrgb()
{
    # Blue and yellow purple tabs...
    echo -en "\033]6;1;bg;*;default\a"
    echo -en "\033]6;1;bg;red;brightness;${1}\a"
    echo -en "\033]6;1;bg;green;brightness;${2}\a"
    echo -en "\033]6;1;bg;blue;brightness;${3}\a"
}


function tabcolor()
{
    MYFUNCNAME="$FUNCNAME"
    function tabcolor_usage() {
        echo "Usage: ${MYFUNCNAME} [random|purple|blue|lightblue|darkblue|orange|green|lightgreen|darkgreen|red|gold|brown|lightbrown|shitbrown]" >&2
        kill -INT $$
        return 1
    }

    function set_tab_default()
    {
        echo -en "\033]6;1;bg;*;default\a"
    }

    COLOR="$1"

    # Aliases
    [ -z "$COLOR" ] && COLOR="random"
    [ "$COLOR" = "brightblue" ] && COLOR="lightblue"
    [ "$COLOR" = "brightgreen" ] && COLOR="lightgreen"
    [ "$COLOR" = "shitbrown" ] && COLOR="brown"

    case "$COLOR" in
        "purple") tabrgb 155 48 255 ;;
        "blue") tabrgb 81 134 255 ;;
        "lightblue") tabrgb 30 144 255 ;;
        "darkblue") tabrgb 0 0 205 ;;
        "orange") tabrgb 255 153 51 ;;
        "green") tabrgb 0 204 0 ;;
        "lightgreen") tabrgb 124 252 0 ;;
        "darkgreen") tabrgb 34 139 34 ;;
        "pink") tabrgb 255 51 183 ;;
        "red") tabrgb 255 51 51 ;;
        "gold") tabrgb 255 215 0 ;;
        "brown") tabrgb 134 34 11 ;;
        "lightbrown") tabrgb 205 133 63 ;;
        "default") set_tab_default ;;
        "random")
            tabrgb \
                "$(od -A n -N 1 -t u2 /dev/urandom)" \
                "$(od -A n -N 1 -t u2 /dev/urandom)" \
                "$(od -A n -N 1 -t u2 /dev/urandom)"
        ;;
        *) tabcolor_usage ;;
    esac
}
# Set personal aliases, overriding those provided by Oh My Zsh libs,
# plugins, and themes. Aliases can be placed here, though Oh My Zsh
# users are encouraged to define aliases within a top-level file in
# the $ZSH_CUSTOM folder, with .zsh extension. Examples:
# - $ZSH_CUSTOM/aliases.zsh
# - $ZSH_CUSTOM/macos.zsh
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
source /Users/ro/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
